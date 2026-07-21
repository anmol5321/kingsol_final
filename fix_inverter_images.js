const fs = require('fs');
const path = require('path');

const workingInverterImg = "https://images.unsplash.com/photo-1548337138-e87d889cc369?auto=format&fit=crop&w=800&q=80";
const brokenImgTarget = "photo-1620027136027-e3f322c2a5bf";

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let totalUpdated = 0;
let totalReplacements = 0;

files.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    if (content.includes(brokenImgTarget)) {
        const regex = /https:\/\/images\.unsplash\.com\/photo-1620027136027-e3f322c2a5bf[^\s"'<>]+/g;
        const matches = content.match(regex);
        const count = matches ? matches.length : 0;
        
        content = content.replace(regex, workingInverterImg);
        fs.writeFileSync(filePath, content, 'utf8');
        
        totalUpdated++;
        totalReplacements += count;
        console.log(`Updated ${file}: ${count} replacements`);
    }
});

console.log(`Finished! Total files: ${totalUpdated}, Total replacements: ${totalReplacements}`);
