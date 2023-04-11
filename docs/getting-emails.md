# Getting email info so you can automate testing involving emails

## Setup

I added an api on the backend to get recently sent emails.  It has to
be turned on before the test and turned off afterwards.  This is an
authenticated endpoint and I need to get the username you will be
using to run the test (not the users involved in the test, but your
username) to add you to the list of users who can invoke the API.
Once you have told me the username I will give you perms to invoke the
API.

## Turning on logging of emails sent

POST to `<hostname>/api/general/setemailtest` with json body with one field `save` that is either `1` to turn on logging or `0` to turn it back off.  E.g., before testing post to above URL with:

```
{
   save: 1
}
```

after testing is done, post to above URL with body of post

```
{
   save: 0
}
```

It will return a json object with `{status: "success"}` if all went well.

## Getting recently sent emails

GET from `<hostname>/api/general/getemaildata` which will return a
json object with two fields `status` and `data`.  `status` needs to be
"success" and `data` is an object with two fields: `info` and `last`.
`info` is an array which represents a circular queue where `last`
points to the next insertion point.  so the most recent email sent
will be in `info[(last-1) mod info.length]`.  the `info` array is
currently set to 10 elements, so older ones will be lost.

E.g.,

```
{
  "status": "success",
  "data": {
    "info": [
      {
        "Destination": {
          "CcAddresses": [],
          "ToAddresses": [
            "seth-m3@cmu.edu"
          ]
        },
        "Source": "info@zuzlab.com",
        "Template": "MerchantVerification",
        "TemplateData": "{\"name\":\"charlie merchant3\"}",
        "ReplyToAddresses": []
      },
      {
        "Destination": {
          "CcAddresses": [],
          "ToAddresses": [
            "seth+testemail@cmu.edu"
          ]
        },
        "Source": "info@zuzlab.com",
        "Template": "EmailVerification",
        "TemplateData": "{\"name\":\"testemail goldstein\",\"verificationLink\":\"https://zuz.me/api/user/verify-email/121?token=240d47167a048184901ebba023c5f1be\"}",
        "ReplyToAddresses": []
      },
      null,
      null,
      null,
      null,
      null,
      null,
      null,
      null
    ],
    "last": 2
  }
}
```

The info you need will be found in `TemplateData` and maybe
`Destination.ToAddresses`.  Each email will have a different format,
but it should be easy to figure out what you need.  E.g., the second
element above has the URL you need to go to in order to verify the new user.

