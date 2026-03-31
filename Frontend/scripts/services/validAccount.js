const BASE_URL = "http://127.0.0.1:8000";

async function validAccount(typeAccount, mail, password) {
    const query = BASE_URL + "/valid/?" + "typeAccount=" + typeAccount + "&mail=" + mail + "&password=" + password;

    const response = await fetch(query);

    if(response.status === 404) {
        throw new Error("No encontrado");
    }

    if(!response.ok) {
        throw new Error("Error HTTP" + response.status);
    }

    const data = await response.json();

    return data
}


// --- EXPORT FUNCTION ---

export async function validAccountService(typeAccount, mail, password) {
    return await validAccount(typeAccount, mail, password)    
}