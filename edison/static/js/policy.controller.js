
import { Policy } from './policy.model.js'

var policy = new Policy();


function createInitElement(type, classSet = '', id = '', style = '') {

    var element = document.createElement(type);

    if (classSet != '') {
        element.setAttribute("class", classSet);
    }
    if (id != '') {
        element.setAttribute("id", id);
    }

    if (style != '') {
        element.setAttribute("style", style);
    }

    return element;
}

function setCondistion() {


    document.getElementById('condition').addEventListener('click', function () {

        var conditionValue = document.getElementById('condition').value;
        var value = document.getElementById('showValue');
        var from = document.getElementById('showFrom');
        var to = document.getElementById('showTo');
        var lableValue = document.getElementById('lableValue');

        if (conditionValue == '=') {
            from.style.display = 'none';
            to.style.display = 'none';
            lableValue.innerHTML = 'Equal';
            value.style.display = 'inline';

        }
        else if (conditionValue == '>' || conditionValue == '<') {

            from.style.display = 'none';
            to.style.display = 'none';
            if (conditionValue == '>') {
                lableValue.innerHTML = 'Above';
            }
            else {
                lableValue.innerHTML = 'Under';
            }
            value.style.display = 'inline';
        }
        else if (conditionValue == 'Between') {

            from.style.display = 'inline';
            to.style.display = 'inline';
            value.style.display = 'none';
        }
        else {
            from.style.display = 'none';
            to.style.display = 'none';
            value.style.display = 'none';
        }

    });
}

function addCondition(policy) {

    var conditionValue = document.getElementById('condition').value;
    var condition = document.getElementById('sensor').value + ' ';

    condition = condition + conditionValue + ' ';


    if (conditionValue == 'Between') {
        condition = condition + document.getElementById('from').value + ' ';
        condition = condition + document.getElementById('to').value;
    }
    else {

        condition = condition + document.getElementById('value').value;
    }

    policy.addCondition(condition);

}


function setCommnad(policy) {

    var light = document.getElementById('light').value;
    var ac = document.getElementById('ac').value;
    var shutters = document.getElementById('shutters').value;

    policy.addCommandToPolicy(ac, light, shutters);

}

function showCondition(policy, countCondition, elementID) {

    var elemet = document.getElementById(elementID);

    var option = createInitElement('option');


    var arrCondotion = policy.condition.split(', ');
    var sensorValue = arrCondotion[countCondition];
    option.innerHTML = countCondition + 1 + ': ' + sensorValue;

    elemet.appendChild(option);

}

function addPolicy() {

    setCondistion();

    var countCondition = 0;

    document.getElementById('saveCondition').addEventListener('click', function () {

        addCondition(policy);
        showCondition(policy, countCondition, 'conditionNum');

        countCondition++;

    });

    document.getElementById('savePolicy').addEventListener('click', function () {
        policy.name = document.getElementById('PolicyName').value;
        policy.room = document.getElementById('choiceRoom').value;

        setCommnad(policy);
        console.log(policy);

        $.post('/policy', policy, function(){});

        policy.reset();

    });

}

$(function () {
    addPolicy();

});
