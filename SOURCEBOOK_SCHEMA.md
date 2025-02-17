# Sourcebook JSON Schema Documentation

This document details the structure and requirements for sourcebook JSON files that can be imported into the D&D Character Builder.

## Schema Overview

```json
{
  "metadata": {
    "title": "Player's Handbook",
    "abbreviation": "PHB",
    "version": "1.0",
    "publisher": "Wizards of the Coast",
    "releaseDate": "2014-08-19",
    "license": "OGL 1.0"
  },
  "content": {
    "races": [...],
    "classes": [...],
    "backgrounds": [...],
    "spells": [...],
    "equipment": [...],
    "features": [...]
  }
}
```

## Detailed Schema

### Races

```json
{
  "races": [
    {
      "name": "Dwarf",
      "description": "Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal.",
      "abilityScoreIncrease": {
        "constitution": 2
      },
      "age": {
        "maturity": 18,
        "maxAge": 350,
        "description": "Dwarves mature at the same rate as humans..."
      },
      "size": {
        "category": "Medium",
        "height": {
          "base": 44,
          "modifier": "2d4"
        },
        "weight": {
          "base": 130,
          "modifier": "2d6"
        }
      },
      "speed": {
        "walk": 25
      },
      "traits": [
        {
          "name": "Darkvision",
          "description": "You can see in dim light within 60 feet of you as if it were bright light...",
          "mechanics": {
            "range": 60,
            "type": "vision"
          }
        }
      ],
      "languages": {
        "standard": ["Common", "Dwarvish"],
        "bonus": {
          "count": 0,
          "options": []
        }
      },
      "subraces": [
        {
          "name": "Hill Dwarf",
          "description": "As a hill dwarf, you have keen senses and deep intuition...",
          "abilityScoreIncrease": {
            "wisdom": 1
          },
          "traits": [
            {
              "name": "Dwarven Toughness",
              "description": "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.",
              "mechanics": {
                "type": "hp_bonus",
                "value": 1,
                "scaling": "level"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### Classes

```json
{
  "classes": [
    {
      "name": "Fighter",
      "description": "A master of martial combat, skilled with a variety of weapons and armor.",
      "hitDie": "d10",
      "primaryAbility": ["strength", "dexterity"],
      "savingThrows": ["strength", "constitution"],
      "proficiencies": {
        "armor": ["light", "medium", "heavy", "shields"],
        "weapons": ["simple", "martial"],
        "tools": [],
        "skills": {
          "count": 2,
          "options": [
            "Acrobatics",
            "Animal Handling",
            "Athletics",
            "History",
            "Insight",
            "Intimidation",
            "Perception",
            "Survival"
          ]
        }
      },
      "startingEquipment": {
        "default": [
          {
            "choice": [["chainmail"], ["leather armor", "longbow", "arrows:20"]]
          }
        ],
        "gold_alternative": "5d4*10"
      },
      "levelFeatures": {
        "1": [
          {
            "name": "Fighting Style",
            "description": "You adopt a particular style of fighting as your specialty...",
            "choices": [
              {
                "name": "Archery",
                "description": "You gain a +2 bonus to attack rolls you make with ranged weapons.",
                "mechanics": {
                  "type": "attack_bonus",
                  "value": 2,
                  "conditions": ["ranged_weapon"]
                }
              }
            ]
          }
        ]
      }
    }
  ]
}
```

### Backgrounds

```json
{
  "backgrounds": [
    {
      "name": "Acolyte",
      "description": "You have spent your life in service to a temple...",
      "proficiencies": {
        "skills": ["Insight", "Religion"],
        "tools": [],
        "languages": {
          "count": 2,
          "options": []
        }
      },
      "equipment": [
        "holy symbol",
        "prayer book",
        "5 sticks of incense",
        "vestments",
        "common clothes",
        "pouch:15gp"
      ],
      "feature": {
        "name": "Shelter of the Faithful",
        "description": "As an acolyte, you command the respect of those who share your faith..."
      },
      "characteristics": {
        "personalityTraits": [
          "I idolize a particular hero of my faith...",
          "I can find common ground between the fiercest enemies..."
        ],
        "ideals": [
          {
            "description": "Faith. I trust that my deity will guide my actions...",
            "alignments": ["Lawful"]
          }
        ],
        "bonds": ["I would die to recover an ancient relic of my faith..."],
        "flaws": ["I judge others harshly, and myself even more severely..."]
      }
    }
  ]
}
```

### Spells

```json
{
  "spells": [
    {
      "name": "Fireball",
      "level": 3,
      "school": "Evocation",
      "castingTime": "1 action",
      "range": {
        "value": 150,
        "unit": "feet"
      },
      "components": {
        "verbal": true,
        "somatic": true,
        "material": {
          "required": true,
          "items": "a tiny ball of bat guano and sulfur",
          "consumed": false,
          "cost": null
        }
      },
      "duration": "Instantaneous",
      "description": "A bright streak flashes from your pointing finger...",
      "higherLevels": {
        "description": "When you cast this spell using a spell slot of 4th level or higher...",
        "scaling": {
          "type": "damage",
          "dice": "1d6",
          "per_level": 1
        }
      },
      "classes": ["Sorcerer", "Wizard"],
      "ritual": false,
      "mechanics": {
        "damage": {
          "base": "8d6",
          "type": "fire"
        },
        "saveType": "dexterity",
        "areaOfEffect": {
          "type": "sphere",
          "size": 20
        }
      }
    }
  ]
}
```

### Equipment

```json
{
  "equipment": {
    "weapons": [
      {
        "name": "Longsword",
        "type": "martial melee",
        "cost": {
          "value": 15,
          "unit": "gp"
        },
        "damage": {
          "diceCount": 1,
          "diceValue": 8,
          "type": "slashing"
        },
        "weight": 3,
        "properties": ["versatile"],
        "versatileDamage": {
          "diceCount": 1,
          "diceValue": 10,
          "type": "slashing"
        }
      }
    ],
    "armor": [
      {
        "name": "Chain Mail",
        "type": "heavy",
        "cost": {
          "value": 75,
          "unit": "gp"
        },
        "armorClass": {
          "base": 16,
          "dexBonus": false
        },
        "strength": 13,
        "stealth": "disadvantage",
        "weight": 55
      }
    ]
  }
}
```

## Validation Rules

1. **Required Fields**

   - All objects must include required name and description fields
   - Classes must specify hitDie and primaryAbility
   - Spells must include level, school, and components

2. **Value Constraints**

   - Ability score increases must be between -2 and +4
   - Spell levels must be 0-9
   - Equipment costs must be positive numbers

3. **Referential Integrity**
   - All referenced classes, races, etc. must exist in the sourcebook
   - Subclass features must reference valid class levels
   - Spell lists must reference valid spells

## Example Usage

```bash
# Import a sourcebook
curl -X POST http://localhost:8000/api/v1/sourcebooks/import \
  -H "Content-Type: multipart/form-data" \
  -F "file=@players_handbook.json"
```

## Best Practices

1. **Modularity**

   - Split large sourcebooks into logical chunks
   - Use consistent naming conventions
   - Include version information

2. **Documentation**

   - Include descriptive text for all features
   - Document any special rules or exceptions
   - Provide usage examples where appropriate

3. **Validation**
   - Test JSON files before import
   - Validate against the schema
   - Check for duplicate entries
