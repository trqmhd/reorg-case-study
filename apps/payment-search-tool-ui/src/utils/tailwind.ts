/**
 * Tailwindui classname mapping.
 * 
 * @param classes 
 * @returns string
 */
function classNames(...classes: any) {
  return classes.filter(Boolean).join(' ')
}

export {
  classNames
}