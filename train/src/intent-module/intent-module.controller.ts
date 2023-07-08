import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { IntentModuleService } from './intent-module.service';
import { CreateIntentModuleDto } from './dto/create-intent-module.dto';

@Controller('train')
export class IntentModuleController {
  constructor(private readonly intentModuleService: IntentModuleService) {}

  @Post()
  create(@Body() module: CreateIntentModuleDto) {
    if (!module?.language) throw new Error('language?');
    return this.intentModuleService.intents(module.language);
  }
}
