
import { Policy } from './policy.model.js'
import { PolicyElementsModifier } from './policyElementsModifier.js'

var policy = new Policy();
var countCondition = 0;
var json_arr_demo = [];
var policyTest1 = new Policy('Test Policy One', 'living room', 'light On, shutters Off', 'humidity < 40, tempetrue < 25');
var policyTest2 = new Policy('Test Policy Two', 'kichen', 'shutters Off', 'humidity > 80, tempetrue between 30 50');
json_arr_demo.push(policyTest1);
json_arr_demo.push(policyTest2);

function setCardBody(policy) {
    var cardBody = createInitElement('div', 'card-body');
    var cardTitle = createInitElement('h5', 'card_title');
    var cardText = createInitElement('h5');
    
    cardBody.appendChild(cardTitle);
    cardBody.appendChild(cardText);
    cardText.innerHTML = "this policy is setting to the " + policy.room + " and the policy do " + policy.command + ' with these conditions: ' + policy.condition;
    return cardBody;
}

function createCard(policyNum, policy) {
    var card = createInitElement('div', 'card');
    var cardHeader = createInitElement('div', 'card-header');
    var hFive = createInitElement('h5', 'mb-0');
    var buttonCradHead = createInitElement('button', 'btn btn-link');

    card.appendChild(cardHeader);
    cardHeader.appendChild(hFive);
    buttonCradHead.setAttribute("data-toggle", "collapse");
    buttonCradHead.setAttribute("data-target", "#collapsePolicy" + policyNum);
    buttonCradHead.setAttribute("aria-expanded", "true");
    buttonCradHead.setAttribute("aria-controls", "collapsePolicy" + policyNum);
    buttonCradHead.innerHTML = policy.name;
    hFive.appendChild(buttonCradHead);
    return card;
}

function showPolicies() {
    $.get('/policy','json');
    var len = json_arr_demo.length;
    var showPolicies = document.getElementById('showPolicies');

    for (var i = 0; i < len; i++) {
        var card = createCard(i, json_arr_demo[i]);
        var collapseClassPolicy = createInitElement("div", "collapse", "collapsePolicy" + i);
        var cardBody = setCardBody(json_arr_demo[i]);

        collapseClassPolicy.setAttribute("aria-labelledby", "headPolicy" + i);
        collapseClassPolicy.setAttribute("data-parent", "#showPolicies");
        showPolicies.appendChild(card);
        card.appendChild(collapseClassPolicy);
        collapseClassPolicy.appendChild(cardBody);
    }
}

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
    showPolicies();
});
