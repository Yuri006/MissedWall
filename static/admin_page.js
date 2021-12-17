import $ from "./jquery.module.js";
function generate_table(users) {
    let table = document.createElement("table");
    let table_name = document.createElement('tr');
    let tn = document.createElement('tn')
    tn.textContent = 'Control panel'
    table_name.appendChild(tn)
    table.appendChild(table_name)
    for (let i = 0; i < users.length + 1; i++) {
        let tr = document.createElement('tr');
        for (let j in users[0]) {
            let td = document.createElement('td');
            if (i == 0) {
                td.textContent = j;
            } else {
                if (j == 6) {
                    td.id = users[i]['id'];
                }
                td.textContent = users[i][j];
            }
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    console.log(table)
    // document.body.appendChild(table);
    return table
}

function get_users() {
    let url = "/cgi-bin/user/list";

    $.get(url, function (data) {
        alert("Data Loaded: " + data);
    });
}

function click_block(id) {
    let url = "/cgi-bin/users_block" + id.toString() + "?" + document.cookie;

    $.get(url, function (data) {
        alert("Data Loaded: " + data);
    });
}

function click_unblock(id) {
    let url = "/cgi-bin/users_unblock" + id.toString() + "?" + document.cookie;

    $.get(url, function (data) {
        alert("Data Loaded: " + data);
    });
}
