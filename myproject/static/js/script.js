const btnTable = document.getElementById('btn-table')
const tableData = document.getElementById('table-data')
const arrowBtn = document.getElementById('arrow-table')
const chart = document.getElementById('chartContainer')
const filterBtn = document.getElementById('filter-btn')
const filterTbl = document.getElementById('filter-table')
const btnMenu = document.getElementById('menu-btn')
const sidebar = document.getElementById('header')

btnTable.addEventListener('click', () => {
  tableData.classList.toggle('-translate-x-full')
  arrowBtn.classList.toggle('rotate-180')
})

// btnMenu.addEventListener('click', () => {
//   sidebar.classList.toggle('-translate-x-full')
//   console.log(';asdipojasd')
// })

filterBtn.addEventListener('click', () => {
  filterTbl.classList.toggle('hidden')
})

filterTbl.addEventListener('click', (e) => {
  if (e.target === filterTbl) {
    filterTbl.classList.add('hidden')
  }
})



