/***
 * Script to update the attend button to attending if a user is 
 * already attending an event
 */

// Start by checking whether request user is authenticated
const username = document.getElementById("usernamePara").innerText;
if(username.length > 0){
    // Get paragraphs containing lists of attendees
    const attendeesParas = document.getElementsByClassName('attendees');
    // Loop through checking for request user
    for(let para of attendeesParas){
        // Get pk of event being displayed
        let paraText = para.innerText
        let paraEventId = para.id
        let eventId = paraEventId.substring(9)
        // Avoid doing this if no attendees
        if(paraText.length > 0){
            // Test whether user is attending event
            if(paraText.includes(username)){
                // Now set button to attending rather than attend
                document.getElementById(`attend${eventId}`).innerText = "Attending"
            }
        }
    }
}


