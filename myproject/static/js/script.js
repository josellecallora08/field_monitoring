const btnTable = document.getElementById('btn-table')
const tableData = document.getElementById('table-data')
const arrowBtn = document.getElementById('arrow-table')
const chart = document.getElementById('chartContainer')
const filterBtn = document.getElementById('filter-btn')
const filterTbl = document.getElementById('filter-table')

filterBtn.addEventListener('click', () => {
  filterTbl.classList.toggle('hidden')
})

filterTbl.addEventListener('click', (e) => {
  if (e.target === filterTbl) {
    filterTbl.classList.add('hidden')
  }
})

btnTable.addEventListener('click', () => {
    tableData.classList.toggle('-translate-x-full')
    arrowBtn.classList.toggle('rotate-180')
    chart.classList.toggle('-z-50')
    console.log('hello')
})


