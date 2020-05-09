
export class Policy {
    constructor() {
        this.name = '';
        this.room = '';
        this.command = '';
        this.condition = '';
    }

    reset() {
        this.name = '';
        this.room = '';
        this.command = '';
        this.condition = '';
    }

    addCondition(add_condition) {
        if (this.condition !== '') {
            this.condition = this.condition + ', ';
        }

        this.condition = this.condition + add_condition;
    }

    addCommandToPolicy(ac, light, shutters) {
        if (light) {
            this.command = this.command + 'light ' + light;
        }

        if (ac) {
            this.command = this.command + ' ,ac ' + ac;
        }

        if (shutters) {
            this.command = this.command + ',shutters ' + shutters;
        }
    }
}
