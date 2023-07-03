import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { IntentModuleModule } from './intent-module/intent-module.module';
import { TypeOrmModule } from '@nestjs/typeorm';
require('dotenv').config();

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DB_HOST,
      port: 5432,
      username: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_NAME,
      ssl: true,
      entities: [
        __dirname + '/**/*.entity{.ts,.js}'
      ],
      synchronize: false,
    }),
    IntentModuleModule,
  ],
  controllers: [AppController],
})
export class AppModule {}
