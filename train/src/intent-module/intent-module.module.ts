import { Module } from '@nestjs/common';
import { IntentModuleService } from './intent-module.service';
import { IntentModuleController } from './intent-module.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ClasificatorModel, Intent, Pattern } from './entities/intent-module.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([Intent, Pattern, ClasificatorModel]),
  ],
  controllers: [IntentModuleController],
  providers: [IntentModuleService]
})
export class IntentModuleModule {}
