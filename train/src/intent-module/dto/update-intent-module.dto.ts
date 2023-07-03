import { PartialType } from '@nestjs/mapped-types';
import { CreateIntentModuleDto } from './create-intent-module.dto';

export class UpdateIntentModuleDto extends PartialType(CreateIntentModuleDto) {}
