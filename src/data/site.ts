export const site = {
  name: 'Infonorm',
  domain: 'infonorm.nl',
  owner: {
    name: 'Friso Smit',
    firstName: 'Friso',
  },
  email: 'info@infonorm.nl',
  phone: '',
  city: 'Noordwijkerhout',
  country: 'Nederland',
  location: 'Noordwijkerhout, Nederland',
  serviceArea: 'Noordwijkerhout en omgeving',
  serviceAreaOr: 'Noordwijkerhout of omgeving',
  whatsapp: 'Op aanvraag via e-mail',
  responseTime: 'Meestal binnen één werkdag',
  linkedin: {
    url: 'https://www.linkedin.com/in/friso-smit-884a19445/',
    label: 'Friso Smit',
  },
} as const;

export function mailto(subject = '') {
  const address = `mailto:${site.email}`;
  return subject ? `${address}?subject=${encodeURIComponent(subject)}` : address;
}

export const emailLinks = {
  general: mailto(),
  advice: mailto(`Adviesaanvraag via ${site.domain}`),
  solar: mailto('Gratis adviesgesprek zonnepanelen'),
} as const;
