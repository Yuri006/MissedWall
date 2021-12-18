/* import $ from "./jquery.module.js"; */
import $ from "./jquery.module.js";

export function checking_nickname() {
    let nick = document.getElementById('nick-field').value
    /* console.log(nick) */
    let url = "/cgi-bin/user_check?nick=" + nick;
    if (nick != ''){
        $.get(url, function (data) {
        if (data == '0') {
            document.getElementById('nick-field').style.backgroundColor = '#e7a1a7' /* #b96e78 */
        } else {
            document.getElementById('nick-field').style.backgroundColor = '#e5e5e5'
        }
        /* console.log(data) */
    });
    } else {
        document.getElementById('nick-field').style.backgroundColor = '#e5e5e5'
    }

}

