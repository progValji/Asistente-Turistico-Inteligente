const input = document.getElementById("ciudad-input");
const lista = document.getElementById("sugerencias");
const listaSugerencias = document.querySelector('.search__quick-picks');

let debounceTimer;

input.addEventListener("input", () => {
  document.getElementById("ciudad-lat").value = "";
  document.getElementById("ciudad-lon").value = "";

  clearTimeout(debounceTimer);
  const query = input.value.trim();

  if (query.length < 2) {
    lista.innerHTML = "";
    return;
  }

  // Espera 500ms después de que el usuario deje de escribir
  debounceTimer = setTimeout(async () => {
    const res = await fetch(`/buscar-ciudades?q=${encodeURIComponent(query)}`);
    const ciudades = await res.json();

    lista.innerHTML = "";
    ciudades.forEach(ciudad => {
      const li = document.createElement("li");
      li.classList.add('search__suggestions-element');
      li.textContent = ciudad.display;
      li.addEventListener("click", () => {
        input.value = ciudad.nombre;
        document.getElementById("ciudad-lat").value = ciudad.lat;
        document.getElementById("ciudad-lon").value = ciudad.lon;
        lista.innerHTML = "";
        document.querySelector('.search__suggestions').classList.remove('search__suggestions--visible');
      });
      lista.appendChild(li);
    });
    document.querySelector('.search__suggestions').classList.add('search__suggestions--visible');
  }, 500);
});

// Cierra sugerencias si el usuario hace click afuera
document.addEventListener("click", (e) => {
  if (!e.target.closest(".search__autocomplete")) {
    document.querySelector('.search__suggestions').classList.remove('search__suggestions--visible');
    lista.innerHTML = "";
  }
});

// Evento para botones de ciudades rápidas
listaSugerencias.addEventListener('click', function(e){
  const boton = e.target.closest('.search__quick-pick');
  
  if (!boton) return;
  
  input.value = boton.textContent.trim();
  document.getElementById("ciudad-lat").value = boton.dataset.lat;
  document.getElementById("ciudad-lon").value = boton.dataset.lon;
});

// Validación del formulario
document.querySelector(".search__form").addEventListener("submit", (e) => {
  const lat = document.getElementById("ciudad-lat").value;
  const lon = document.getElementById("ciudad-lon").value;

  if (!lat || !lon) {
    e.preventDefault();
    document.querySelector('.modal-sugerencias').showModal();
    input.focus();
  }
});