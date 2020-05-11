
import { Policy } from './policy.model.js'
export class PoliciesExampleArray {

    constructor() {
        this.examples = [];
        this.modify();
    }

    modify() {
        var policyTest1 = new Policy('Test Policy One', 'living room', 'light On, shutters Off', 'humidity < 40, tempetrue < 25');
        var policyTest2 = new Policy('Test Policy Two', 'kichen', 'shutters Off', 'humidity > 80, tempetrue between 30 50');
        this.examples.push(policyTest1);
        this.examples.push(policyTest2);
    }
}
