'use strict'

const openModal = () => document.getElementById('modal')
    .classList.add('active')

const closeModal = () => {
    clearFields()
    document.getElementById('modal').classList.remove('active')
}


const getLocalStorage = () => JSON.parse(localStorage.getItem('db_livro')) ?? []
const setLocalStorage = (dbBiblioteca) => localStorage.setItem("db_livro", JSON.stringify(dbBiblioteca))

// CRUD - create read update delete
const deleteBiblioteca = (index) => {
    const dbBiblioteca = readBiblioteca()
    dbBiblioteca.splice(index, 1)
    setLocalStorage(dbBiblioteca)
}

const updateBiblioteca = (index, livro) => {
    const dbBiblioteca = readBiblioteca()
    dbBiblioteca[index] = livro
    setLocalStorage(dbBiblioteca)
}

const readBiblioteca = () => getLocalStorage()

// CREATE 
const createBiblioteca = (livro) => {
    const dbBiblioteca = getLocalStorage()
    dbBiblioteca.push (livro)
    setLocalStorage(dbBiblioteca)
}

const isValidFields = () => {
    return document.getElementById('form').reportValidity()
}

//Interação com o layout

const clearFields = () => {
    const fields = document.querySelectorAll('.modal-field')
    fields.forEach(field => field.value = "")
    document.getElementById('nome').dataset.index = 'new'
    document.querySelector(".modal-header>h2").textContent  = 'Novo Livro'
}

const saveBiblioteca = () => {
    if (isValidFields()) {
        const livro = {
            nome: document.getElementById('nome').value,
            autor: document.getElementById('autor').value,
            genero: document.getElementById('genero').value,
            paginasTotais: document.getElementById('paginasTotais').value,
            paginasLidas: document.getElementById('paginasLidas').value,
            anotacoes: document.getElementById('anotacoes').value
        }
        const index = document.getElementById('nome').dataset.index
        if (index == 'new') {
            createBiblioteca(livro)
            updateTable()
            clearFields()
            closeModal()
        } else {
            updateBiblioteca(index, livro)
            updateTable()
            clearFields()
            closeModal()
        }
    }
}

const createRow = (livro, index) => {
    const newRow = document.createElement('tr')
    newRow.innerHTML = `
        <td>${livro.nome}</td>
        <td>${livro.autor}</td>
        <td>${livro.genero}</td>
        <td>${livro.paginasTotais}</td>
        <td>${livro.paginasLidas}</td>
        <td>${livro.anotacoes}</td>
        <td>
            <button type="button" class="button green" id="edit-${index}">Editar</button>
            <button type="button" class="button red" id="delete-${index}" >Excluir</button>
        </td>
    `
    document.querySelector('#tableLivro>tbody').appendChild(newRow)
}

const clearTable = () => {
    const rows = document.querySelectorAll('#tableLivro>tbody tr')
    rows.forEach(row => row.parentNode.removeChild(row))
}

// toda vez que a tela carregar, os dados vão aparecer 

const updateTable = () => {
    const dbBiblioteca = readBiblioteca()
    clearTable()
    dbBiblioteca.forEach(createRow)
}

const fillFields = (livro) => {
    document.getElementById('nome').value = livro.nome
    document.getElementById('autor').value = livro.autor
    document.getElementById('genero').value = livro.genero
    document.getElementById('paginasTotais').value = livro.paginasTotais
    document.getElementById('paginasLidas').value = livro.paginasLidas
    document.getElementById('anotacoes').value = livro.anotacoes
    document.getElementById('nome').dataset.index = livro.index
}

const editBiblioteca = (index) => {
    const livro = readBiblioteca()[index]
    livro.index = index
    fillFields(livro)
    document.querySelector(".modal-header>h2").textContent  = `Editando ${livro.nome}`
    openModal()
}

const editDelete = (event) => {
    if (event.target.type == 'button') {

        const [action, index] = event.target.id.split('-')

        if (action == 'edit') {
            editBiblioteca(index)
        } else {
            const livro = readBiblioteca()[index]
            const response = confirm(`Deseja realmente excluir o livro ${livro.nome} ?`)
            if (response) {
                deleteBiblioteca(index)
                updateTable()
            }
        }
    }
}

updateTable()

// Eventos
document.getElementById('cadastrarLivro')
    .addEventListener('click', openModal)

document.getElementById('modalClose')
    .addEventListener('click', closeModal)

document.getElementById('salvar')
    .addEventListener('click', saveBiblioteca)

document.querySelector('#tableLivro>tbody')
    .addEventListener('click', editDelete)

document.getElementById('cancelar')
    .addEventListener('click', closeModal)