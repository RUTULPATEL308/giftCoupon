// function validatePhoneNumber(input_str) {
//     var re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;

//     return re.test(input_str);
// }

// function validateForm(event) {
//     var phone = document.getElementById('myform_phone').value;
//     if (!validatePhoneNumber(phone)) {
//         document.getElementById('phone_error').classList.remove('hidden');
//     } else {
//         document.getElementById('phone_error').classList.add('hidden');
//         alert("validation success")
//     }
//     event.preventDefault();
// }




// Below Function Executes On Form Submit
function ValidationEvent() {
    // Storing Field Values In Variables
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var contact = document.getElementById("myform_phone").value;
    var code = document.getElementById("code").value;
    var uid = document.getElementById("upid").value;
    // Regular Expression For Email
    var emailReg = /^([w-.]+@([w-]+.)+[w-]{2,4})?$/;
    var re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;
    // Conditions
    if (name != '' && email != '' && contact != '' && code != '' && uid != '') {
        if (email.match(emailReg)) {
            
                if (contact.length == 10 && contact.match(re)) {
                    alert("All type of validation has done on OnSubmit event.");
                    document.getElementById('contactForm').addEventListener('submit', validateForm);
                    return true;
                } else {
                    alert("The Contact No. must be at least 10 digit long!");
                    return false;
                }
        } else {
            alert("Invalid Email Address...!!!");
            return false;
        }
    } else {
        alert("All fields are required.....!");
        return false;
    }
}
