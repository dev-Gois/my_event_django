const deleteEvent = (button) => {
  const eventUrl = button.getAttribute('data-url');
  
  return Swal.fire({
    title: 'Você tem certeza?',
    text: "Você não poderá reverter isso!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    cancelButtonText: 'Cancelar',
    confirmButtonText: 'Sim, deletar!'
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = eventUrl;
    }
  });
}