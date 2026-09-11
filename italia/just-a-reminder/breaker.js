const CryptoJS = require("crypto-js");

const ciphertext = "U2FsdGVkX1/JEKDXgPl2RqtEgj0LMdp8/Q1FQelH7whIP49sq+WvNOeNjjXwmdrl";
const secretKey = "ML4czctKUzigEeuR"; // Busca esta variable en el JS de la página

const bytes = CryptoJS.AES.decrypt(ciphertext, secretKey);
const password = bytes.toString(CryptoJS.enc.Utf8);

console.log("Contraseña:", password);
