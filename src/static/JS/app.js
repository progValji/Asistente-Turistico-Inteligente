  const input = document.getElementById("ciudad-input");
  const lista = document.getElementById("sugerencias");
  const listaSugerancia = document.querySelector('.search__quick-picks')

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
        li.classList.add('search-suggetions__element')
        li.textContent = ciudad.display;        // "Orizaba, Veracruz"
        li.addEventListener("click", () => {
          input.value = ciudad.nombre;
          document.getElementById("ciudad-lat").value = ciudad.lat;
          document.getElementById("ciudad-lon").value = ciudad.lon;
          lista.innerHTML = "";
        });
        lista.appendChild(li);
      });
      document.querySelector('.search__suggestions').classList.add('search__suggestions--visible')
    }, 500);

  });

  // Cierra sugerencias si el usuario hace click afuera
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".autocomplete-wrapper")) {
      document.querySelector('.search__suggestions').classList.remove('search__suggestions--visible')
      lista.innerHTML = "";
    }
  });

  listaSugerancia.addEventListener('click', function(e){
  const boton = e.target.closest('.search__quick-pick');

  if (!boton) return;

  input.value = boton.textContent.trim()
  document.getElementById("ciudad-lat").value = boton.dataset.lat
  document.getElementById("ciudad-lon").value = boton.dataset.lon
  })

  document.querySelector(".search__form").addEventListener("submit", (e) => {
    const lat = document.getElementById("ciudad-lat").value;
    const lon = document.getElementById("ciudad-lon").value;

    if (!lat || !lon) {
      e.preventDefault(); // cancela el envío
      document.querySelector('.modal-sugerencias').showModal()
      input.focus();
    }
  });