#!/usr/bin/env python3

import subprocess

KEYTOOL_PATH = 'apksigner'

def get_sha256_cert_fingerprint(apk):
    apk_cert = subprocess.Popen(
        KEYTOOL_PATH + ' verify --print-certs ' + apk, shell=True, stdout=subprocess.PIPE
    ).stdout.read().decode()
    print(apk_cert)
    if 'SHA-256 digest: ' in apk_cert:
        components = apk_cert.split('1 certificate SHA-256 digest: ')
        print(components)
        if len(components) > 1:
            return components[1].split('\n')[0]
    return None 
