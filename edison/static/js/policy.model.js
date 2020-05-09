
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

    addCommandToPolicy(airConditioner, light, shutters) {
        var sensors = []; 
        if (light) {
            sensors.push('light ' + light);
        }

        if (airConditioner) {
            sensors.push('air conditioner ' + airConditioner);;
        }

        if (shutters) {
            sensors.push('shutters ' + shutters);
        }
        this.command = sensors.join(' ,');
    }
}
