import { Policy } from './policy.model.js';
import { PolicyElementsModifier } from './policyElementsModifier.js';
import { PoliciesExampleArray } from './policiesExampleArray.js';

var policy = new Policy();

function capitalize(string) {
  if (typeof string !== 'string') return '';
  return `${string.charAt(0).toUpperCase()}${string.slice(1)}`;
}

function createTextElementForUpdate(id, fieldName, field) {
  var _id = `policy-${fieldName}${id}`;
  var groupName = createInitElement('div', 'form-group');
  var labelName = createInitElement('label');
  var inputName = createInitElement('input', 'form-control', _id);
  var label = capitalize(fieldName);

  labelName.setAttribute('for', _id);
  labelName.innerHTML = label;
  groupName.appendChild(labelName);
  inputName.setAttribute('type', 'text');
  inputName.setAttribute('placeholder', field);
  groupName.appendChild(inputName);

  return groupName;
}
function createUpdateButton(classButton, id) {
  var updateButton = createInitElement('button', classButton, id);

  updateButton.innerHTML = 'Update';
  updateButton.setAttribute('data-toggle', 'collapse');
  updateButton.setAttribute('data-target', `#collapse-${id}`);
  updateButton.setAttribute('type', 'false');
  updateButton.setAttribute('aria-expanded', 'button');
  updateButton.setAttribute('aria-controls', `collapse-${id}`);

  return updateButton;
}

function setCardBody(policy) {
  var cardBody = createInitElement('div', 'card-body');
  var cardTitle = createInitElement('h5', 'card_title');
  var cardText = createInitElement('h5');
  var updateButton = createUpdateButton(
    'btn btn-primary',
    `update-policy${policy.id}`
  );
  var headerUpdateButton = createInitElement(
    'div',
    'collapse',
    `collapse-update-policy${policy.id}`
  );
  var cardBodyUpdateButton = createInitElement('div', 'card card-body update');
  var nameField = createTextElementForUpdate(policy.id, 'name', policy.name);
  var roomField = createTextElementForUpdate(policy.id, 'room', policy.room);

  cardBody.appendChild(cardTitle);
  cardBody.appendChild(cardText);
  cardBody.appendChild(updateButton);
  cardBody.appendChild(headerUpdateButton);
  headerUpdateButton.appendChild(cardBodyUpdateButton);
  cardBodyUpdateButton.appendChild(nameField);
  cardBodyUpdateButton.appendChild(roomField);
  cardText.innerHTML = `This policy is associated with ${policy.room} room and responsible for ${policy.command}
    with these conditions: ${policy.condition}`;

  return cardBody;
}

function createCard(policy) {
  var card = createInitElement('div', 'card');
  var headerCard = createInitElement('div', 'card-header');
  var buttonTextSize = createInitElement('h5', 'mb-0');
  var headerCardButton = createInitElement('button', 'btn btn-link');

  card.appendChild(headerCard);
  headerCard.appendChild(buttonTextSize);
  headerCardButton.setAttribute('data-toggle', 'collapse');
  headerCardButton.setAttribute('data-target', `#collapse-policy${policy.id}`);
  headerCardButton.setAttribute('aria-expanded', 'true');
  headerCardButton.setAttribute('aria-controls', `collapse-policy${policy.id}`);
  headerCardButton.innerHTML = policy.name;
  buttonTextSize.appendChild(headerCardButton);

  return card;
}

function getFromBackend() {
  //once the route will be ready this function will be modifiy to get the policies from the backend and convert them to array
  var jsonPolicyExample = new PoliciesExampleArray().jsonPolicesExample;
  var policiesArray = [];

  for (var i in jsonPolicyExample) {
    var newPolicy = new Policy(
      jsonPolicyExample[i].name,
      jsonPolicyExample[i].room,
      jsonPolicyExample[i].command,
      jsonPolicyExample[i].condition,
      jsonPolicyExample[i].id
    );
    policiesArray.push(newPolicy);
  }

  return policiesArray;
}

function showPolicies() {
  var policiesArray = getFromBackend();
  var len = policiesArray.length;
  var showPolicies = document.getElementById('show-policies');
  for (var i = 0; i < len; i++) {
    var card = createCard(policiesArray[i]);
    var collapseClassPolicy = createInitElement(
      'div',
      'collapse',
      `collapse-policy${policiesArray[i].id}`
    );
    var cardBody = setCardBody(policiesArray[i]);

    collapseClassPolicy.setAttribute(
      'aria-labelledby',
      `head-policy${policiesArray[i].id}`
    );
    collapseClassPolicy.setAttribute('data-parent', '#show-policies');
    showPolicies.appendChild(card);
    card.appendChild(collapseClassPolicy);
    collapseClassPolicy.appendChild(cardBody);
  }
}

function createInitElement(type, className = '', id = '') {
  var element = document.createElement(type);

  if (className !== '') {
    element.setAttribute('class', className);
  }

  if (id !== '') {
    element.setAttribute('id', id);
  }
  return element;
}

function setCondition() {
  var policyElementsModifier = new PolicyElementsModifier();
  var conditionValue = document.getElementById('choose-condition').value;
  var equalOrUnderOrAbove = document.getElementById('show-equal-under-above');
  var from = document.getElementById('show-from');
  var to = document.getElementById('show-to');
  var labelEqualOrUnderOrAbove = document.getElementById(
    'label-equal-under-above'
  );

  policyElementsModifier.modify(
    conditionValue,
    from,
    to,
    labelEqualOrUnderOrAbove,
    equalOrUnderOrAbove
  );
}

function addCondition(policy) {
  var conditionValue = document.getElementById('choose-condition').value;
  var sensor = `${document.getElementById('sensor').value} `;

  var condition = `${sensor + conditionValue} `;

  if (conditionValue === 'Between') {
    condition = `${condition + document.getElementById('from').value} `;
    condition = `${condition + document.getElementById('to').value}`;
  } else {
    condition = `${
      condition + document.getElementById('equal-under-above').value
    }`;
  }

  policy.addCondition(condition);
}

function setCommand(policy) {
  var light = document.getElementById('light').value;
  var airConditioner = document.getElementById('air-conditioner').value;
  var shutters = document.getElementById('shutters').value;

  policy.addCommandToPolicy(airConditioner, light, shutters);
}

function showCondition(policy, countCondition, elementID) {
  var element = document.getElementById(elementID);
  var elementCurrCondition = createInitElement(
    'option',
    '',
    `option${countCondition}`
  );
  var arrCondition = policy.condition.split(', ');
  var currCondition = arrCondition[countCondition - 1];

  elementCurrCondition.innerHTML = `${countCondition}: ${currCondition} `;
  element.appendChild(elementCurrCondition);
}

function initSettingToNewPolicy() {
  var len = policy.getCountCondition();

  for (var i = 1; i <= len; i++) {
    var element = document.getElementById(`option${i}`);
    element.remove();
  }

  policy.reset();
}

function addPolicy() {
  policy.name = document.getElementById('policy-name').value;
  policy.room = document.getElementById('policy-room').value;
  setCommand(policy);
  // var jsonPolicy = {
  //   policy_name: policy.name,
  //   room: policy.room,
  //   commands: policy.command,
  //   conditions: policy.condition,
  // };
  //this function will be enable when the route wiil be ready
  //$.post('/policy/new_policy', json, function(){ },"json");
  initSettingToNewPolicy();
}

function saveCondition() {
  addCondition(policy);
  var countCondition = policy.getCountCondition();
  showCondition(policy, countCondition, 'condition-list');
}

function mainFunctionPolicy() {
  document
    .getElementById('choose-condition')
    .addEventListener('click', setCondition);
  document
    .getElementById('save-condition')
    .addEventListener('click', saveCondition);
  document.getElementById('save-policy').addEventListener('click', addPolicy);
}

$(function () {
  mainFunctionPolicy();
  showPolicies();
});
