import { Policy } from './policy.model.js'
export class PoliciesExampleArray {

    constructor() {
        this.jsonPolicesExample = [{
            'id': '1',
            'name': 'Test Policy One',
            'room': 'living',
            'command': 'light On, shutters Off',
            'condition': 'humidity < 40, tempetrue < 25'
        }, {
            'id': '2',
            'name': 'Test Policy Two',
            'room': 'kitchen',
            'command': 'shutters Off',
            'condition': 'humidity > 80, tempetrue between 30 50'
        },{
            'id': '3',
            'name': 'Test Policy Three',
            'room': 'bad',
            'command': 'shutters Off',
            'condition': 'humidity > 80, tempetrue between 30 50'
        }];
    }
}
