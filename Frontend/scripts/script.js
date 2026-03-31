
import { validAccountService } from "./services/validAccount.js";


// getDataService().then(data => {
//     console.log(data);
// });

// getDataByService("mail","carlos@mail.com").then(data => {
//         console.log(data)
// })

document.getElementById('login').addEventListener('submit',async function(event) {
    event.preventDefault();
    const typeAccount = document.querySelector('input[name="typeAccount"]:checked').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const data = await validAccountService(typeAccount, email, password);

        console.log(data);

        if (!data.ok) {
            console.error("Error backend:", data.error);
            return;
        }

        if (!data.data || data.data.length === 0) {
            console.log("mail no registrado");
            return;
        }

        console.log("mail registrado");

    } catch (error) {
        console.error(error);
    }

});