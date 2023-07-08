import { Entity, PrimaryGeneratedColumn, Column, OneToMany, ManyToOne, JoinColumn, PrimaryColumn } from 'typeorm';

@Entity('intents')
export class Intent {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  intent: string;

  @OneToMany(() => Response, (response) => response.intent)
  responses: Response[];
}

@Entity('clasificatorModel')
export class ClasificatorModel {
  @PrimaryColumn()
  id: string;

  @Column('json')
  model: any;

  @Column()
  language: string;

  @Column({ type: 'timestamp', precision: 3 })
  createdat: Date;
}

@Entity('responses')
export class Response {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  response: string;

  @Column()
  intentid: number;

  @Column()
  language: string;

  @Column()
  clasificator: string;

  @ManyToOne(() => Intent, (intent) => intent.responses)
  @JoinColumn({ name: 'intentid' })
  intent: Intent;
}