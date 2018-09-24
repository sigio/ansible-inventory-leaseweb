# ansible-inventory-leaseweb
Leaseweb Cloud Inventory script for ansible

This script uses the Leaseweb (v2) api to gather information about virtual machines
hosted in the Leaseweb cloud.

It needs an API-Key, which can be created in the leaseweb webinterface, to be present
as LEASEWEB_API_KEY environment variable

The 'reference' field in the virtual-machine info is used as 'hostname'.
