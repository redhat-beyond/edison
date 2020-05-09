
export class PolicyElementsModifier {
    #configByCondition;

    constructor() {
        this.#configByCondition = {
            '=': { displayTo: 'none', displayFrom: 'none', labelValue: 'Equal', displayValue: 'inline' },
            '<': { displayTo: 'none', displayFrom: 'none', labelValue: 'Under', displayValue: 'inline' },
            '>': { displayTo: 'none', displayFrom: 'none', labelValue: 'Above', displayValue: 'inline' },
            'Between': { displayTo: 'inline', displayFrom: 'inline', labelValue: '', displayValue: 'none' }
        }
    }

    modify(condition, from, to, labelValue, value) {
        if (this.#configByCondition.hasOwnProperty(condition)) {
            var config = this.#configByCondition[condition];
            to.style.display = config.displayTo;
            from.style.display = config.displayFrom;
            value.style.display = config.displayValue;
            labelValue.innerHTML = config.labelValue;
        }
    }
}
