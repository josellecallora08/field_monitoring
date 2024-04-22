const btnTable = document.getElementById('btn-table')
const tableData = document.getElementById('table-data')
const arrowBtn = document.getElementById('arrow-table')
const chart = document.getElementById('chartContainer')

btnTable.addEventListener('click', () => {
    tableData.classList.toggle('-translate-x-full')
    arrowBtn.classList.toggle('rotate-180')
    chart.classList.toggle('-z-50')
    console.log('hello')
})

