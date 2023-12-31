import { Injectable } from '@nestjs/common';
import { CreateAuthDto } from './dto/create-auth.dto';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';
import { v4 as uuidv4 } from 'uuid';
import { UserService } from 'src/user/user.service';
import { User } from 'src/user/entities/user.entity';

enum Role {
  MASTER = 'master',
  ADMIN = 'admin',
  USER = 'user',
}

// class User {
//   id: string;
//   email: string;
//   passwordHash: string;
//   role: string;
//   constructor(auth: {email: string, hash: string, role: Role}) {
//     this.id = uuidv4();
//     this.email = auth.email;
//     this.passwordHash = auth.hash;
//     this.role = auth.role;
//   }
// }

@Injectable()
export class AuthService {
  private systemUsers: User[] = [];  
  constructor(
    private readonly userService: UserService,
    private readonly jwtService: JwtService) {}

  async hashing(password: string): Promise<string> {
    try {
      return await bcrypt.hash(password, 10);  
    } catch (error) {
      throw new Error(`Name: ${error.name}, message: ${error.message}, password: ${password}`);
    }
  }

  async register(createAuthDto: CreateAuthDto) {

    const providedUser = await this.userService.getOneByEmail(createAuthDto.email);
    console.log(JSON.stringify(providedUser));

    if (providedUser) {
      throw new Error('user error');
    }

    const passwordHash = await this.hashing(createAuthDto.password);
    console.log(`Password ${createAuthDto.password} hash is ${passwordHash}.`);

    const user = new User({
      email: createAuthDto.email,
      passwordHash,
      role: Role.MASTER,
    });
    await this.userService.create(user);

    console.table(this.systemUsers);
    return {};
  }

  async login(email: string, password: string) {
    const providedUser = await this.userService.getOneByEmail(email);
    if (!providedUser) {
      throw new Error('user error');
    }
    
    if (!await(bcrypt.compare(password, providedUser.passwordHash))) throw new Error(`bsc`);
    const token = await this.generateToken(providedUser.id);
    return {
      token,
    };
  }

  async generateToken(userId: string): Promise<string> {
    return await this.jwtService.signAsync({ id: userId });
  }

  async jwtTokenCheck(token) {
    try {
      const decoded = this.jwtService.verify(token['authorization']?.split(' ')[1]);
      const user: User = await this.userService.getOne(decoded.id);

      if (!user) throw new Error('no such user');
      return {
        permision: 'allowed',
        userId: user.id,
        role: user.role,
      }

      
    } catch (error) {
      throw new Error('jwt error');
    }
  }
}
