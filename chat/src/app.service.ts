import { Injectable } from '@nestjs/common';
import { BayesClassifier, Tokenizer } from 'natural';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { ClasificatorModel, Intent } from './entity';
const natural = require('natural');

@Injectable()
export class AppService {
  private intents;
  private tokenizer;
  private classifier;

  constructor(
    @InjectRepository(Intent)
    private intentRepository: Repository<Intent>,
    @InjectRepository(ClasificatorModel)
    private modelRepository: Repository<ClasificatorModel>,
  ) {
    // this.trainModel();
    this.tokenizer = new natural.WordTokenizer();
    this.classifier = new natural.BayesClassifier();
  }

  async chat({ language, phrase}) {
    const status = await this.feed(language);
    return this.classifyUserInput(phrase, language);
  }

  async feed(language: string) {
    const modelML = await this.modelRepository.findOneBy({ language });
    if (!modelML) {
      throw new Error(`Cant load model`);
    }

    this.classifier = BayesClassifier.restore(modelML.model);
    if (!this.classifier) {
      throw new Error(`Cant load this.classifier`);
    }

    const data1 = await this.intentRepository
      .createQueryBuilder("intents")
      .leftJoinAndSelect("intents.responses", "responses")
      .where("responses.language = :language", { language })
      .getMany();
    
    if (!data1) {
      throw new Error(`Cant load intents`);
    }

    this.intents = { i: this.getFormatedIntents(data1) };
  }

  getFormatedIntents(data) {
    const formedIntentions = [];
    for (let i = 0; i < data.length; i++) {
      let iterationResponses = [];

      for (let a = 0; a < data[i].responses.length; a++) {
        iterationResponses.push(data[i].responses[a]);
      }

      formedIntentions.push({
        intent: data[i].intent,
        responses: iterationResponses,
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

  

  classifyUserInput(userInput: string, language: string) {
    
    const tokens = this.tokenizer.tokenize(userInput.toLowerCase());
    console.log(`Tokens: ${tokens}`);


    const predictedIntent = this.classifier.classify(tokens);
    console.log(`Intent predicted: ${predictedIntent}`);

    const intent = this.intents.i.find(intent => intent.intent === predictedIntent);
    

    // const randomResponse = intent ? intent.responses[Math.floor(Math.random() * intent.responses.length)] : null;
    return {
      predicted_answers: intent.responses,
      predicted_intent: intent.intent,
      tokens,
    }
    
  }
}
