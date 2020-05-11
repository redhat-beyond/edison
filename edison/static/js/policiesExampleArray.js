import { Policy } from './policy.model.js'
export class PoliciesExampleArray {

    constructor() {
        this.jsonPolicesExample = [{
            'id': '1',
            'name': 'Test Policy One',
            'room': 'living room',
            'command': 'light On, shutters Off',
            'condition': 'humidity < 40, tempetrue < 25'
        }, {
            'id': '2',
            'name': 'Test Policy Two',
            'room': 'kichen',
            'command': 'shutters Off',
            'condition': 'humidity > 80, tempetrue between 30 50'
        }];
    }
}
