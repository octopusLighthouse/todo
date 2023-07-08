import { Body, Controller, Get, Post } from '@nestjs/common';
import { AppService } from './app.service';

@Controller('chat')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Post()
  async create(@Body() module) {
    if (!module?.phrase) throw new Error('phrase?');
    if (!module?.language) throw new Error('language?');
    return await this.appService.chat(module);
  }
}
