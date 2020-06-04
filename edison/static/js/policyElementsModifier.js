export class PolicyElementsModifier {
  #configByCondition;

  constructor() {
    this.#configByCondition = {
      '=': {
        displayTo: 'none',
        displayFrom: 'none',
        labelEqualOrUnderOrAbove: 'Equal',
        displayEqualOrUnderOrAbove: 'inline',
      },
      '<': {
        displayTo: 'none',
        displayFrom: 'none',
        labelEqualOrUnderOrAbove: 'Under',
        displayEqualOrUnderOrAbove: 'inline',
      },
      '>': {
        displayTo: 'none',
        displayFrom: 'none',
        labelEqualOrUnderOrAbove: 'Above',
        displayEqualOrUnderOrAbove: 'inline',
      },
      Between: {
        displayTo: 'inline',
        displayFrom: 'inline',
        labelEqualOrUnderOrAbove: '',
        displayEqualOrUnderOrAbove: 'none',
      },
    };
  }

  modify(condition, from, to, labelEqualOrUnderOrAbove, equalOrUnderOrAbove) {
    if (this.#configByCondition.hasOwnProperty(condition)) {
      var config = this.#configByCondition[condition];

      to.style.display = config.displayTo;
      from.style.display = config.displayFrom;
      equalOrUnderOrAbove.style.display = config.displayEqualOrUnderOrAbove;
      labelEqualOrUnderOrAbove.innerHTML = config.labelEqualOrUnderOrAbove;
    }
  }
}
