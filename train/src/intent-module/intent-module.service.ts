import { Injectable } from '@nestjs/common';
import { CreateIntentModuleDto } from './dto/create-intent-module.dto';
import { UpdateIntentModuleDto } from './dto/update-intent-module.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { ClasificatorModel, Intent, Pattern } from './entities/intent-module.entity';
const natural = require('natural');
import { v4 as uuidv4 } from 'uuid';
import * as moment from 'moment';


@Injectable()
export class IntentModuleService {
  private tokenizer;
  private classifier;

  constructor(
    @InjectRepository(Intent)
    private intentRepository: Repository<Intent>,
    @InjectRepository(ClasificatorModel)
    private modelRepository: Repository<ClasificatorModel>,
  ) {
    this.tokenizer = new natural.WordTokenizer();
    this.classifier = new natural.BayesClassifier();
  }
  
  async intents(language: string) {
    const data = await this.intentRepository
      .createQueryBuilder("intents")
      .leftJoinAndSelect("intents.patterns", "patterns")
      .where("patterns.language = :language", { language })
      .getMany();

    return await this.train(this.getFormatedIntents(data), language);
  }

  getFormatedIntents(data) {
    const formedIntentions = [];
    for (let i = 0; i < data.length; i++) {
      let iterationPatterns = [];

      for (let a = 0; a < data[i].patterns.length; a++) {
        iterationPatterns.push(data[i].patterns[a].pattern);
      }

      formedIntentions.push({
        intent: data[i].intent,
        patterns: iterationPatterns,
      });
    }

    return formedIntentions;

    // return [
    //   { intent: 'greeting', patterns: ['hello', 'hi', 'hey'], responses: ['Hello!', 'Hi there!', 'Hey! How can I assist you?'] },
    //   { intent: 'menu', patterns: ['menu', 'what do you offer'], responses: ['We offer a variety of coffees, teas, and pastries. What would you like to order?'] },
    //   { intent: 'order', patterns: ['I would like to order', 'Can I get a'], responses: ['Sure, what would you like to order?', 'Of course, what can I get for you?'] },
    //   { intent: 'goodbye', patterns: ['bye', 'goodbye', 'see you later'], responses: ['Goodbye!', 'See you later!', 'Take care!'] },
    //   { intent: 'fallback', patterns: [''], responses: ['Sorry, I didn\'t understand that. Could you please rephrase?'] }
    // ];
  }

  async train(intents, language: string) {
    const trainingData = intents.flatMap(intent =>
      intent.patterns.map(
        pattern => (
          { 
            tokens: this.tokenizer.tokenize(pattern.toLowerCase()), 
            intent: intent.intent,
          }
        )
      )
    );
    
    // Train the classifier
    trainingData.forEach(
      data => this.classifier.addDocument(
        data.tokens, 
        data.intent,
      )
    );
    this.classifier.train();

    const trainedModelByProvidedLanguage = {
      id: uuidv4(),
      model: this.classifier,
      language,
      createdat: moment().utc().toDate(),
    }

    console.table(trainedModelByProvidedLanguage);

    try {
      const updated = await this.modelRepository.update({ language }, trainedModelByProvidedLanguage);
      if (updated.affected === 0)  {
        await this.modelRepository.save(trainedModelByProvidedLanguage);
      }
      console.table(updated);
    } catch (error) {
      
    }
    

    
    // await this.modelRepository.save(md);
    // Classify user input and generate a response
    return this.classifier;
  }
}
