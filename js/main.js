var json = (function () {
    var json = null;
    $.ajax({
        'async': false,
        'global': false,
        'url': './data/data.json',
        'dataType': "json",
        'success': function (data) {
            json = data;
        }
    });
    return json;
})();


function get_topping(json) {
    return json.Toppings[Math.floor(Math.random() * json.Toppings.length)];
}

function get_milk_tea(json) {
    return json["Milk Tea"][Math.floor(Math.random() * json["Milk Tea"].length)];
}

function get_fruit_tea(json) {
    return json["Fruit Tea"][Math.floor(Math.random() * json["Fruit Tea"].length)];
}

function get_ice_tea(json) {
    return json["Ice Tea"][Math.floor(Math.random() * json["Ice Tea"].length)];
}

function display_tea_options_html(json) {
    var mydiv = document.getElementById("dropDownTea");
    var newElement = document.createElement('div');
    var str = ''
    for (let k in json) {
        if (k !== "Toppings") {
            let option = document.createElement("option");
            option.text = k;
            option.value = k;
            let select = document.getElementById("dropDownTea");
            select.appendChild(option);
        }
    }

    newElement.innerHTML = str;
    mydiv.appendChild(newElement);
}

function what_tea(tea) {
    if (tea === "Milk Tea") {
        return get_milk_tea(json);
    }
    if (tea === "Fruit Tea") {
        return get_fruit_tea(json);
    }
    if (tea === "Ice Tea") {
        return get_ice_tea(json);
    }

}

function get_tea(event) {
    // Gets symbol and time and places them into a hidden input field
    if (event.target.id !== 'dropDownTea') {
        return null;
    }
    if (event.target.id === 'dropDownTea') {
        document.getElementById("dropDownTea").value = event.target.value;
    }
    if (document.getElementById("dropDownTea").value !== "") {
        let tea_ = document.getElementById("dropDownTea").value;
        var tea = what_tea(tea_);
        let topping1 = get_topping(json);
        let topping2 = get_topping(json);
        document.getElementById("randomTea").innerHTML = `${tea}, with ${topping1} and ${topping2}`;
        document.getElementById("divDropDownTea").hidden = true;
        document.getElementById("dropDownTea").hidden = true;
        document.getElementById("tryAgain").hidden = false;
    }
}

display_tea_options_html(json);
window.addEventListener('input', get_tea, false);

function copyright_update() {
    var today = new Date();
    var year = today.getFullYear();
    var paragraph = document.getElementById("copyright");
    paragraph.innerHTML = 'Copyright &copy; ' + year + ' <a href="https://github.com/KonScanner">KonScanner</a><br>All Rights Reserved';
}
copyright_update();