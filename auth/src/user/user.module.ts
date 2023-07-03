<<<<<<< HEAD
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { userController } from './user.controller';
import { UserService } from './user.service';
import { User } from './entities/user.entity';
import { UserRepository } from './user.repository';

@Module({
	imports: [
		TypeOrmModule.forFeature([
			User,
		]),
	],
	controllers: [
		userController,
	],
	providers: [
		UserService,
		UserRepository,
	],
	exports: [
		UserService,
	]
})
export class UserModule {}
=======
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { userController } from './user.controller';
import { UserService } from './user.service';
import { User } from './entities/user.entity';
import { UserRepository } from './user.repository';

@Module({
	imports: [
		TypeOrmModule.forFeature([
			User,
		]),
	],
	controllers: [
		userController,
	],
	providers: [
		UserService,
		UserRepository,
	],
	exports: [
		UserService,
	]
})
export class UserModule {}
>>>>>>> 301111d518bb2e036389ca433f95e73821f33627
