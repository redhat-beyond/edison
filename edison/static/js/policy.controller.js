
import { Policy } from './policy.model.js'
import { PolicyElementsModifier } from './policyElementsModifier.js'

var policy = new Policy();
var countCondition = 0;

function createInitElement(type, classSet = '', id = '', style = '') {
    var element = document.createElement(type);

    if (classSet !== '') {
        element.setAttribute("class", classSet);
    }

    if (id !== '') {
        element.setAttribute("id", id);
    }

    if (style !== '') {
        element.setAttribute("style", style);
    }

    return element;
}

function setCondition() {
    var policyElementsModifier = new PolicyElementsModifier();
    var conditionValue = document.getElementById('condition').value;
    var value = document.getElementById('showValue');
    var from = document.getElementById('showFrom');
    var to = document.getElementById('showTo');
    var labelValue = document.getElementById('labelValue');

    policyElementsModifier.modify(conditionValue, from, to, labelValue, value);
}

function addCondition(policy) {
    var conditionValue = document.getElementById('condition').value;
    var condition = document.getElementById('sensor').value + ' ';

    condition = condition + conditionValue + ' ';

    if (conditionValue === 'Between') {
        condition = condition + document.getElementById('from').value + ' ';
        condition = condition + document.getElementById('to').value;
    } else {
        condition = condition + document.getElementById('value').value;
    }

    policy.addCondition(condition);
}

function setCommand(policy) {
    var light = document.getElementById('light').value;
    var ac = document.getElementById('ac').value;
    var shutters = document.getElementById('shutters').value;

    policy.addCommandToPolicy(ac, light, shutters);
}

function showCondition(policy, countCondition, elementID) {
    var element = document.getElementById(elementID);
    var option = createInitElement('option', '', 'option' + countCondition);
    var arrCondition = policy.condition.split(', ');
    var sensorValue = arrCondition[countCondition];

    option.innerHTML = countCondition + 1 + ': ' + sensorValue;
    element.appendChild(option);
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
    policy.name = document.getElementById('PolicyName').value;
    policy.room = document.getElementById('choiceRoom').value;
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
    document.getElementById('condition').addEventListener('click', setCondition);
    document.getElementById('saveCondition').addEventListener('click', saveCondition);
    document.getElementById('savePolicy').addEventListener('click', addPolicy);
}

$(function () {
    mainFunctionPolicy();
});
