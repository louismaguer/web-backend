document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('form').forEach((form) => {
        const formToJSON = form => Object.fromEntries(new FormData(form))
        form.addEventListener("submit", async (event) => {

          // the default behaviour (sending form data as urlencoded) is
          // precisely what we DON'T WANT, so we prevent it
          event.preventDefault()

          // convert the form data into a plain JavaScript object
          const json = formToJSON(form)

          // use the action= and method= attributes
          //  to determine where to send the data
          const {action, method} = form
          const response = await fetch(action, {
            method,
            headers: {
              "Content-Type": "application/json",
              "Accept": "application/json",
            },
            body: JSON.stringify(json),
          })
          if (!response.ok) {
            console.error(`Error submitting form at ${action} : `,
              response.statusText)
            return
          }
          const decoded = await response.json()
          console.log("response", decoded)
        })
      })
    })
