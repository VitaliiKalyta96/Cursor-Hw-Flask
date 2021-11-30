// $(document).ready(function () {
//     $("#searchInput").on('keyup', function (event) {
//         let text = $(this).val();
//         console.log(text);
//     })
// });



const searchResults = document.getElementById('searchResults');
const searchInput = document.getElementById('searchInput');
let hpCharacters = [];

searchInput.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();
        console.log(searchString);
    const filteredCharacters = hpCharacters.filter((character) => {
        return (
            character.name.toLowerCase().includes(searchString) ||
            character.location.toLowerCase().includes(searchString)
        );
    });
    displayCharacters(filteredCharacters);
});

const loadCharacters = async () => {
    try {
        const res = await fetch('http://localhost:9092/plant/1');
        hpCharacters = await res.json();
        displayCharacters(hpCharacters);
    } catch (err) {
        console.error(err);
    }
};

// const fetcher = () => {
//     console.log(searchString);
//         fetch(`http://localhost:9092/plant/${id}`)
//             .then(response => console.log(response))
//             .then(data => console.log(data))
//             .catch(error => console.error('Unable to get items.', error));
//  }
// fetcher()

const displayCharacters = (characters) => {
    const htmlString = characters
        .map((character) => {
            return `
            <div class="character">
                <label ${character.name}</label>
            </div>
            <div class="character">
                <label ${character.location}</label>
            </div>
        `;
        })
        .join('');
    charactersList.innerHTML = htmlString;
};

loadCharacters();



// https://www.jamesqquick.com/blog/build-a-javascript-search-bar

