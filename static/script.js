function call() {
    let clg_name = document.getElementById("clg_name").value;
    let prof_name = document.getElementById("prof_name").value;
    let prof_email = document.getElementById("prof_email").value;
    let phone = document.getElementById("phone").value;
    let t_name = document.getElementById("t_name").value;
    let student_name1 = document.getElementById("student_name1").value;
    let student_name2 = document.getElementById("student_name2").value;
    let t_number = document.getElementById("t_number").value;
    let email = document.getElementById("email").value;
    // let passwd = document.getElementById("passwd").value;
    let auth = document.getElementById("auth").value;

    // console.log(url + " " + name);

    let payload = {
        "clg_name": clg_name,
        "prof_name": prof_name,
        "prof_email": prof_email,
        "phone": phone,
        "t_name": t_name,
        "student_name1": student_name1,
        "student_name2": student_name2,
        "t_number": t_number,
        "email": email,
        // "passwd": passwd,
        "auth": auth
    };

    if (clg_name === "" && clg_name.length === 0) {
        alert("Input value can not be empty");
        return
    }else if (prof_name === "" && prof_name.length === 0) {
        alert("Input value can not be empty string.");
        return
    }else if (prof_email === "" && prof_email.length === 0) {
        alert("Input value can not be empty string.");
        return
    }else if (phone === "" && phone.length >= 10) {
        alert("Invalid phone number.");
        return
    }else if (t_name === "" && t_name.length === 0) {
        alert("Input value can not be empty string.");
        return
    }else if (student_name1 === "" && student_name1.length === 0) {
        alert("Input value can not be empty string.");
        return
    }else if (student_name2 === "" && student_name2.length === 0) {
        alert("Input value can not be empty string.");
        return
    }else if (t_number === "" && t_number.length >= 10) {
        alert("Invalid phone number.");
        return
    }else if (email === "" && email.length === 0) {
        alert("Input value can not be empty string.");
        return
    }else if (auth === "" && auth.length === 0) {
        alert("Input value can not be empty string.");
        return
    }


    // http_request.open("POST", url_api, true);
    let config = {
        url: '/authorize',
        baseURL: 'http://127.0.0.1:5000',
        method: 'POST',
        data: JSON.stringify(payload),
        headers: {
            "Content-Type": "application/json"
        }
    };

    console.log(JSON.stringify(payload));

    axios(config)
        .then(function (response) {
            console.log(response.data);
            if (response.data["status"] === 1) {
                console.log("its string");
                alert("username: "+ response.data['username']+"\npassword: "+response.data["password"]);
                alert("Username and password sent to your team email and professor's email..")
                window.location.replace('http://127.0.0.1:5000');
            } else {
                console.log("Error occurred.")
            }
        })

        .catch(function (error) {
            console.log(error);
        });
    // http_request.setRequestHeader("Content-type", "application/json");
    // http_request.send(JSON.stringify(payload));

}