# Jitsi re0rchestrator API

Jitsi reOrchestartor API for Kubernetes. The purpose of this API is to run and manage more than one Jitsi-Meet on a kubernetes cluster.


## Architecture

![architecture_image](https://github.com/muazdervent/jitsi-re0rchestrator-api/blob/main/architecture_image.png?raw=true)

## Installation and explanation

Please follow README.md in **installation** folder.

## WARNING!

This project was created only to show that the system can be implemented. It is your responsibility to ensure the security of the system. 

## Usage
You can use the created deployments by forwarding the required port with Jitsi Meet Api.

You can also use this api with [moodle-mod_jitsi](https://github.com/muazdervent/moodle-mod_jitsi).

- Send request to API for deploying Jitsi:

http://your_domain_or_ip:3000/jitsi?operation=create&parameter=daily_meeting_13 (session uniq id)

- or destroy deployment:

http://your_domain_or_ip:3000/jitsi?operation=destroy&parameter=30200 (session web port)

- or delete video record:

http://your_domain_or_ip:3000/jitsi?operation=delete_video_record&parameter=123 (record id)

- Access to database:

your_domain_or_ip:30306

## License
GPL v3 License
