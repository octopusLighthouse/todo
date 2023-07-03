import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ClasificatorModel, Intent, Response } from './entity';
require('dotenv').config();

@Module({
  imports: [
    TypeOrmModule.forFeature([Intent, Response, ClasificatorModel]),
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: process.env.DB_HOST,
      port: 5432,
      username: process.env.DB_USER,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_NAME,
      ssl: true,
      entities: [
        __dirname + '/entity{.ts,.js}'
      ],
      synchronize: false,
    }),
    
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
