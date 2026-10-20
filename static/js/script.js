document.addEventListener("DOMContentLoaded", function () {
    const inputBusqueda = document.getElementById("input-busqueda");
    const selectCategoria = document.getElementById("select-categoria");
    const selectSintoma = document.getElementById("select-sintoma");
    const selectRiesgo = document.getElementById("select-riesgo");
    const btnLimpiar = document.getElementById("btn-limpiar");
    const btnSubir = document.getElementById("btn-subir");

    const seccionesCategorias = document.querySelectorAll(".seccion-categoria");
    // LÓGICA PARA EL BOTÓN DE MODO OSCURO
    const btnModo = document.getElementById("btn-modo-oscuro");
    const iconoModo = document.getElementById("icono-modo");

    // Verificar si el usuario ya tenía activado el modo oscuro previamente
    if (localStorage.getItem("modo-oscuro") === "activado") {
        document.body.classList.add("modo-oscuro");
        if (iconoModo) iconoModo.textContent = "☀️";
        if (btnModo) {
            btnModo.innerHTML = '<span id="icono-modo">☀️</span> Modo Claro';
        }
    }
    if (btnModo) {
        btnModo.addEventListener("click", function () {
            document.body.classList.toggle("modo-oscuro");

            if (document.body.classList.contains("modo-oscuro")) {
                localStorage.setItem("modo-oscuro", "activado");
                btnModo.innerHTML = '<span id="icono-modo">☀️</span> Modo Claro';
            } else {
                localStorage.setItem("modo-oscuro", "desactivado");
                btnModo.innerHTML = '<span id="icono-modo">🌙</span> Modo Oscuro';
            }
        });
    }
    // FUNCIÓN PRINCIPAL PARA FILTRAR LOS EQUIPOS
    function filtrarEquipos() {
        const textoBusqueda = inputBusqueda ? inputBusqueda.value.toLowerCase().trim() : "";
        const categoriaSel = selectCategoria ? selectCategoria.value : "";
        const sintomaSel = selectSintoma ? selectSintoma.value.toLowerCase().trim() : "";
        const riesgoSel = selectRiesgo ? selectRiesgo.value.toLowerCase().trim() : "";

        seccionesCategorias.forEach(seccion => {
            const idCategoriaSeccion = seccion.getAttribute("id");

            // Si seleccionó categoría y no coincide con la sección, ocultarla
            if (categoriaSel !== "" && idCategoriaSeccion !== categoriaSel) {
                seccion.style.display = "none";
                return;
            }

            const tarjetas = seccion.querySelectorAll(".tarjeta");
            let tarjetasVisiblesEnSeccion = 0;

            tarjetas.forEach(tarjeta => {
                const nombre = (tarjeta.getAttribute("data-nombre") || "").toLowerCase();
                const sintomas = (tarjeta.getAttribute("data-sintomas") || "").toLowerCase();
                const riesgo = (tarjeta.getAttribute("data-riesgo") || "").toLowerCase();

                const coincideNombre = textoBusqueda === "" || nombre.includes(textoBusqueda);
                const coincideSintoma = sintomaSel === "" || sintomas.includes(sintomaSel);
                const coincideRiesgo = riesgoSel === "" || riesgo.includes(riesgoSel);

                if (coincideNombre && coincideSintoma && coincideRiesgo) {
                    tarjeta.style.display = "";
                    tarjetasVisiblesEnSeccion++;
                } else {
                    tarjeta.style.display = "none";
                }
            });

            // Si hay equipos visibles, mostrar la sección
            if (tarjetasVisiblesEnSeccion > 0) {
                seccion.style.display = "";
            } else {
                seccion.style.display = "none";
            }
        });
    }

    // Escuchar eventos en los filtros
    [inputBusqueda, selectCategoria, selectSintoma, selectRiesgo].forEach(elemento => {
        if (elemento) {
            elemento.addEventListener("input", filtrarEquipos);
            elemento.addEventListener("change", filtrarEquipos);
        }
    });

    // Acción del botón Limpiar Filtros
    if (btnLimpiar) {
        btnLimpiar.addEventListener("click", function () {
            if (inputBusqueda) inputBusqueda.value = "";
            if (selectCategoria) selectCategoria.value = "";
            if (selectSintoma) selectSintoma.value = "";
            if (selectRiesgo) selectRiesgo.value = "";
            filtrarEquipos();
        });
    }

    // Lógica para el botón flotante "Volver arriba"
    if (btnSubir) {
        window.addEventListener("scroll", function () {
            if (window.scrollY > 300 || document.documentElement.scrollTop > 300) {
                btnSubir.classList.add("visible");
            } else {
                btnSubir.classList.remove("visible");
            }
        });

        btnSubir.addEventListener("click", function () {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
            document.documentElement.scrollTop = 0;
            document.body.scrollTop = 0;
        });
    }
});