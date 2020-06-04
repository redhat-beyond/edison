export class PoliciesExampleArray {
  constructor() {
    this.jsonPolicesExample = [
      {
        id: '1',
        name: 'Test Policy One',
        room: 'living room',
        command: 'light On, shutters Off',
        condition: 'humidity < 40, temperature < 25',
      },
      {
        id: '2',
        name: 'Test Policy Two',
        room: 'kitchen',
        command: 'shutters Off',
        condition: 'humidity > 80, temperature between 30 50',
      },
      {
        id: '3',
        name: 'Test Policy Three',
        room: 'bedroom',
        command: 'shutters Off',
        condition: 'humidity > 80, temperature between 30 50',
      },
    ];
  }
}
