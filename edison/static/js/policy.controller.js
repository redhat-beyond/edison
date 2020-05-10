
import { Policy } from './policy.model.js'
import { PolicyElementsModifier } from './policyElementsModifier.js'

var policy = new Policy();
var countCondition = 0;

function createInitElement(type, className = '', id = '') {
    var element = document.createElement(type);

    if (className !== '') {
        element.setAttribute("class", className);
    }

    if (id !== '') {
        element.setAttribute("id", id);
    }
    return element;
}

function setCondition() {
    var policyElementsModifier = new PolicyElementsModifier();
    var conditionValue = document.getElementById('chooseCondition').value;
    var equalOrUnderOrAbove = document.getElementById('showEqualOrUnderOrAbove');
    var from = document.getElementById('showFrom');
    var to = document.getElementById('showTo');
    var labelEqualOrUnderOrAbove = document.getElementById('labelEqualOrUnderOrAbove');

    policyElementsModifier.modify(conditionValue, from, to, labelEqualOrUnderOrAbove, equalOrUnderOrAbove);
}

function addCondition(policy) {
    var conditionValue = document.getElementById('chooseCondition').value;
    var sensor = document.getElementById('sensor').value + ' ';

    var condition = sensor + conditionValue + ' ';

    if (conditionValue === 'Between') {
        condition = condition + document.getElementById('from').value + ' ';
        condition = condition + document.getElementById('to').value;
    } else {
        condition = condition + document.getElementById('equalOrUnderOrAbove').value;
    }

    policy.addCondition(condition);
}

function setCommand(policy) {
    var light = document.getElementById('light').value;
    var airConditioner = document.getElementById('airConditioner').value;
    var shutters = document.getElementById('shutters').value;

    policy.addCommandToPolicy(airConditioner, light, shutters);
}

function showCondition(policy, countCondition, elementID) {
    var element = document.getElementById(elementID);
    var elementCurrCondition = createInitElement('option', '', 'option' + countCondition);
    var arrCondition = policy.condition.split(', ');
    var currCondition = arrCondition[countCondition];

    elementCurrCondition.innerHTML = countCondition + 1 + ': ' + currCondition;
    element.appendChild(elementCurrCondition);
}

function initSettingToNewPolicy() {
    policy.reset();

    for (var i = 0; i < countCondition; i++) {
        var element = document.getElementById('option' + i);

        element.remove();
    }

    countCondition = 0;
}

function addPolicy() {
    policy.name = document.getElementById('policyName').value;
    policy.room = document.getElementById('policyRoom').value;
    setCommand(policy);
    $.post('/policy', policy, function () { });
    initSettingToNewPolicy();
}

function saveCondition() {
    addCondition(policy);
    showCondition(policy, countCondition, 'conditionNum');
    countCondition++;
}

function mainFunctionPolicy() {
    document.getElementById('chooseCondition').addEventListener('click', setCondition);
    document.getElementById('saveCondition').addEventListener('click', saveCondition);
    document.getElementById('savePolicy').addEventListener('click', addPolicy);
}

$(function () {
    mainFunctionPolicy();
});
