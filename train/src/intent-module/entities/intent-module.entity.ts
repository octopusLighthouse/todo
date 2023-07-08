import { Entity, PrimaryGeneratedColumn, Column, OneToMany, ManyToOne, JoinColumn, PrimaryColumn } from 'typeorm';

@Entity('intents')
export class Intent {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  intent: string;

  @OneToMany(() => Pattern, (pattern) => pattern.intent)
  patterns: Pattern[];

  // @OneToMany(() => Response, (response) => response.intent)
  // responses: Response[];
}

@Entity('patterns')
export class Pattern {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  pattern: string;

  @Column()
  intentid: number;

  @Column()
  language: string;

  @ManyToOne(() => Intent, (intent) => intent.patterns)
  @JoinColumn({ name: 'intentid' })
  intent: Intent;
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

// @Entity('responses')
// export class Response {
//   @PrimaryGeneratedColumn()
//   id: number;

//   @Column()
//   response: string;

//   @Column()
//   intentid: number;

//   @Column()
//   language: string;

//   @ManyToOne(() => Intent, (intent) => intent.patterns)
//   @JoinColumn({ name: 'intentid' })
//   intent: Intent;
// }