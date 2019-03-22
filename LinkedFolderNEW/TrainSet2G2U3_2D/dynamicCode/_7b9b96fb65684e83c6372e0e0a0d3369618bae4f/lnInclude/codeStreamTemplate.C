/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | Copyright (C) YEAR AUTHOR,AFFILIATION
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Description
    Template for use with codeStream.

\*---------------------------------------------------------------------------*/

#include "dictionary.H"
#include "Ostream.H"
#include "Pstream.H"
#include "unitConversion.H"

//{{{ begin codeInclude
#line 0 "/mnt/c/Users/Nigel/Documents/NTUFYP2019/NNBasedSteadyStateSurrogateCFD/LinkedFolder/TrainSet2G2U3_2D/system/blockMeshDict.#codeStream"
#include "pointField.H"
//}}} end codeInclude

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C"
{
    void codeStream_7b9b96fb65684e83c6372e0e0a0d3369618bae4f
    (
        Ostream& os,
        const dictionary& dict
    )
    {
//{{{ begin code
        #line 0 "/mnt/c/Users/Nigel/Documents/NTUFYP2019/NNBasedSteadyStateSurrogateCFD/LinkedFolder/TrainSet2G2U3_2D/system/blockMeshDict.#codeStream"
pointField points(16);
        points[0]  = point(0, 0, 0.5);
        points[1]  = point(25.5, 0, 0.5);
        points[2]  = point(25.5, 12.7, 0.5);
        points[3]  = point(0, 12.7, 0.5);
        points[4]  = point(5, 4, 0.5);
        points[5]  = point(6, 4, 0.5);
        points[6]  = point(6, 6, 0.5);
        points[7]  = point(5, 6, 0.5);
        points[8]  = point(5, 0, 0.5);
        points[9]  = point(6, 0, 0.5);
        points[10] = point(25.5, 4, 0.5);
        points[11] = point(25.5, 6, 0.5);
        points[12] = point(6, 12.7, 0.5);
        points[13] = point(5, 12.7, 0.5);
        points[14] = point(0, 6, 0.5);
        points[15] = point(0, 4, 0.5);

        // Duplicate z points
        label sz = points.size();
        points.setSize(2*sz);
        for (label i = 0; i < sz; i++)
        {
            const point& pt = points[i];
            points[i+sz] = point(pt.x(), pt.y(), -pt.z());
        }

        os  << points;
//}}} end code
    }
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

