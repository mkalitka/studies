"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.persons = void 0;
exports.persons = [
    {
        name: 'Jan Kowalski',
        age: 17,
        occupation: 'Student'
    },
    {
        name: 'Tomasz Malinowski',
        age: 20,
        role: 'Administrator'
    }
];
function logPerson(person) {
    let additionalInformation;
    if ("occupation" in person)
        additionalInformation = person.occupation;
    else
        additionalInformation = person.role;
    console.log(` - ${person.name}, ${person.age}, ${additionalInformation}`);
}
exports.persons.forEach(logPerson);
