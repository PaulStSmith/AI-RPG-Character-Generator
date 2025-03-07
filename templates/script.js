$(document).ready(function() {
    // Character data variable to store the JSON data
    let characterData = null;

    // Setup copy button event handlers once on page load
    $('#copy-json').on('click', function() {
        if (characterData) {
            copyToClipboard(JSON.stringify(characterData, null, 2));
            showCopyFeedback();
        }
    });

    $('#copy-html').on('click', function() {
        if ($('#character-sheet').html().trim()) {
            copyToClipboard($('#character-sheet').html());
            showCopyFeedback();
        }
    });

    $('#copy-text').on('click', async function() {
        if ($('#character-sheet').html().trim()) {
            const element = document.getElementById('character-sheet');
            
            try {
                // Use the clipboard API with HTML format
                await navigator.clipboard.write([
                    new ClipboardItem({
                        'text/html': new Blob([element.innerHTML], { type: 'text/html' }),
                        'text/plain': new Blob([element.innerText], { type: 'text/plain' })
                    })
                ]);
                console.log('Content copied with formatting!');
                showCopyFeedback();
            } catch (err) {
                console.error('Failed to copy: ', err);
                $('#copy-failed').fadeIn().delay(1000).fadeOut();
            }
        }
    });

    // Function to show copy feedback
    function showCopyFeedback() {
        $('#copy-feedback').fadeIn().delay(1000).fadeOut();
    }

    // Form submission handler
    $('#character-form').on('submit', function(e) {
        e.preventDefault();
        const prompt = $('#prompt').val();
        $('#loading').show();
        $('#character-sheet').hide();
        $.ajax({
            url: '/generate',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ prompt: prompt }),
            success: function(data) {
                // Store the data for use by copy buttons
                characterData = data;
                
                const characterSheet = `
                    <h2 class="text-center mb-4">${data.name}</h2>
                    <div class="row">
                        <div class="col-md-4">
                            <p><strong>Ancestry:</strong> ${data.ancestry}</p>
                            <p><strong>Background:</strong> ${data.background}</p>
                            <p><strong>Class:</strong> ${data.character_class.name} (Level ${data.level})</p>
                            <p><strong>Alignment:</strong> ${data.alignment}</p>
                        </div>
                        <div class="col-md-4">
                            <p><strong>Hit Points:</strong> ${data.hit_points}</p>
                            <p><strong>Armor Class:</strong> ${data.armor_class}</p>
                            <p><strong>Languages:</strong> ${data.languages.join(', ')}</p>
                        </div>
                        <div class="col-md-4">
                            <h4>Saving Throws</h4>
                            <ul class="list-unstyled">
                                ${Object.entries(data.saving_throws).map(([save, value]) => 
                                    `<li><strong>${save}:</strong> ${value}</li>`
                                ).join('')}
                            </ul>
                        </div>
                    </div>
                    <h3 class="mt-4">Abilities</h3>
                    <div class="row">
                        ${Object.entries(data.abilities).map(([ability, stats]) => `
                            <div class="col-md-2 col-sm-4">
                                <div class="ability-score">
                                    <h4>${ability}</h4>
                                    <p class="mb-0">Score: ${stats.score}</p>
                                    <p class="mb-0">Modifier: ${calculateModifier(stats.score)}</p>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                    <h3 class="mt-4">Skills</h3>
                    <div class="row">
                        ${data.skills.map(skill => `
                            <div class="col-md-3 col-sm-6">
                                <p><strong>${skill.name}:</strong> ${skill.proficiency} (${skill.modifier})</p>
                            </div>
                        `).join('')}
                    </div>
                    <h3 class="mt-4">Feats</h3>
                    <ul>
                        ${data.feats.map(feat => `<li>${feat}</li>`).join('')}
                    </ul>
                    <h3 class="mt-4">Equipment</h3>
                    <ul>
                        ${data.equipment.map(item => `<li>${item}</li>`).join('')}
                    </ul>
                    <h3 class="mt-4">Character Details</h3>
                    <p><strong>Description:</strong> ${data.description}</p>
                    <p><strong>Look:</strong> ${data.look}</p>
                    <p><strong>Way of Speaking:</strong> ${data.way_of_speaking}</p>
                    <p><strong>Loves:</strong> ${data.loves}</p>
                    <p><strong>Hates:</strong> ${data.hates}</p>
                `;
                $('#character-sheet').html(characterSheet);
                $('#loading').hide();
                $('#character-sheet').show();
            },
            error: function() {
                $('#character-sheet').html('<p class="text-danger">Failed to generate character sheet. Please try again.</p>');
                $('#loading').hide();
                $('#character-sheet').show();
            }
        });
    });
});

function calculateModifier(score) {
    return Math.floor((score - 10) / 2);
}

function copyToClipboard(text) {
    const tempInput = document.createElement('textarea');
    tempInput.value = text;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
}
